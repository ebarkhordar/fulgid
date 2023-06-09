class Person:
    def __init__(self):
        self.breathe_in_oxygen()
    
    def breathe_in_oxygen(self):
        self.bronchial_tubes = BronchialTubes()
        self.bronchial_tubes.pass_oxygen_to_lungs()

class BronchialTubes:
    def __init__(self):
        self.lungs = Lungs()
    
    def pass_oxygen_to_lungs(self):
        self.lungs.move_oxygen_into_bloodstream()

class Lungs:
    def __init__(self):
        self.bloodstream = Bloodstream()
    
    def move_oxygen_into_bloodstream(self):
        self.bloodstream.circulate_through_body()

class Bloodstream:
    def __init__(self):
        self.cells = Cells()
    
    def circulate_through_body(self):
        self.cells.exchange_oxygen_with_carbon_dioxide()

class Cells:
    def __init__(self):
        self.bloodstream = Bloodstream()
    
    def exchange_oxygen_with_carbon_dioxide(self):
        self.bloodstream.carry_carbon_dioxide_back_to_lungs()

class Lungs:
    def __init__(self):
        self.person = Person()
    
    def carry_carbon_dioxide_back_to_lungs(self):
        self.person.expel_carbon_dioxide_through_nose_and_mouth()

class Person:
    def __init__(self):
        pass
    
    def expel_carbon_dioxide_through_nose_and_mouth(self):
        pass