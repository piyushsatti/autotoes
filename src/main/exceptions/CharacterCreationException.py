class CharacterCreationException(Exception):
    
    def __init__(self, message, type):            
        super().__init__(message)
        self.type = type