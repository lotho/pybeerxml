import pytest
import os
from pybeerxml import Parser, Recipe
from pybeerxml.hop import Hop
from xml.etree import ElementTree
from math import floor

RECIPE_PATH = os.path.join(os.path.dirname(__file__), "Simcoe IPA.xml")

class TestParser:

    def test_parse(self):

        recipe_parser = Parser()
        recipes = recipe_parser.parse(RECIPE_PATH)

        "should have at least one recipe"
        assert(len(recipes) > 0)

        recipe = recipes[0]

        "should be of type Recipe"
        assert(type(recipe) is Recipe)

        "should have the correct amount of ingriedients"
        assert(len(recipe.hops) == 3)
        assert(len(recipe.yeasts) == 1)
        assert(len(recipe.fermentables) == 2)

        "should have mashing steps"
        assert(len(recipe.mash.steps) == 4)

        "should have the correctly calculated properties"
        assert(round(recipe.og, 4) == 1.0338)
        assert(round(recipe.og_plato, 4) == 8.4815)
        assert(round(recipe.fg, 4) == 1.0047)
        assert(round(recipe.fg_plato, 4) == 1.2156)
        assert(floor(recipe.ibu) == 99)
        assert(round(recipe.abv, 2) == 3.84)

        "should have the correct recipe metadata"
        assert(recipe.name == "Simcoe IPA")
        assert(recipe.brewer == "Tom Herold")
        assert(recipe.efficiency == 76.0)
        assert(recipe.batch_size == 14.9902306488)
        assert(recipe.boil_time == 30.0)

        "should have the correct style metadata"
        assert(recipe.style.name == "American IPA")


    def test_node_to_object(self):
        "test XML node parsing to Python object"

        node = ElementTree.fromstring("""<hop>
            <name>Simcoe</name>
            <alpha>13</alpha>
            <amount>0.5</amount>
            <use>boil</use>
            <time>30</time>
            </hop>""")

        test_hop = Hop()

        recipe_parser = Parser()
        recipe_parser.nodes_to_object(node, test_hop)

        assert test_hop.name, "Simcoe"
        assert test_hop.alpha, 13
        assert test_hop.amount, 0.5
        assert test_hop.use, "boil"
        assert test_hop.time, 30

    def test_to_lower(self):

        recipe_parser = Parser()
        assert(recipe_parser.to_lower("MASH") == "mash")
        assert(recipe_parser.to_lower("") == "")
        assert(recipe_parser.to_lower(10) == "")
        assert(recipe_parser.to_lower(None) == "")




