from pydantic import BaseModel, validator  
from pydantic import EmailStr 
from pydantic import Field
from datetime import datetime, date

class Form(BaseModel):
    firt_name   : str = Field(
        ...,
        min_length  = 1,
        max_length  = 19,
        example     = "MARIANGEL ESTEFANIA"
    )
    password    : str #= Field(
    #     ...,
    #     min_length  = 6,
    #     example     = "Hola123"        
    #)
    last_name   : str
    birth_day   : datetime
    email       : EmailStr
    phone       : int

#### Test validation age

#     # @validator('password')
#     # def password_alphanumeric(cls, v):
#     #     assert v.isalnum(), 'must be alphanumeric'
#     #     return v
# birth_day = input('add ')
#     @validator('birth_day')
#     def calculateAge(cls, v): 
#         today = date.today() 
#         age = today.year - v.year - ((today.month, today.day) < (v.month, v.day)) 
#         if age >= 2004-9-23:
#             print(True)
#             # return age
#         else: 
#             print(False)
#             # raise Exception('No tienes la edad') 