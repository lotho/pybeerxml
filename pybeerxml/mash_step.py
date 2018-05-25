class MashStep(object):
    def __init__(self):
        self.name = None
        self.version = None
        self.type = None
        self.infuse_amount = None
        self.end_temp = None
        self.step_time = None
        self.step_temp = None
        self.decoction_amt = None
        self.description = None
        self.infuse_temp = None
        self.ramp_time = None
        self.water_grain_ratio = None
        self.display_step_temp = None
        self.display_infuse_amt = None

        @property
        def waterRatio(self):
            raise NotImplementedError("waterRation")
            # water_amout = self.infuse_amount or self.decoction_amt
            # return water_amount / recipe.grainWeight()
