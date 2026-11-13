letter = '''Dear <|Name|>,
                        You Are Selected 
                        <|Date|>'''

print(letter.replace("<|Name|>","Mohammed Saad Shaikh").replace("<|Date|>","18th October 2026"))#this is called as a chaining in which there is a seccond replace function in the first replace function 
print(letter.replace("<|Name|>","Saad Shaikh").replace("<|Date|>","16th October 2026"))