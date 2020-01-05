from PyInquirer import Validator, ValidationError

class ItemValidator(Validator):
    def validate(self, document):
        if(str(document.text) == ''):
                raise ValidationError(
                    message='Please enter an item name',
                    cursor_position=len(document.text))