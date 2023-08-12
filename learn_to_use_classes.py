class family:
    def __init__(person, name, gender, upside, first_meet):
        person.name = name
        person.gender = gender
        person.good_point = upside
        person.reason = first_meet

    def how_we_met(person):
        if person.gender == 'girl':
            print('I met', person.name, person.reason + ".", 
                  'She is', person.good_point, 
                  'and I love her for that!')
            
        elif person.gender == 'boy':
            print('I met', person.name, person.reason + ".", 
                  'He is', person.good_point, 
                  'and I love him for that!')
        
        
reason = ('when I offered her my seat,' 
          ' and later she "rewarded" me'
          ' with a tasty cup of sugarcane juice')

My_girl = family('Chau', 'girl', 'a caring person', reason)
My_girl.how_we_met()

Dad = family('Dad', 'boy', 'the wisest man I know', 'when I was born')
Dad.how_we_met()

Mom = family('Mom', 'girl', 
             'the one who feels more pain when I get hurt', 
             'inside her tummy')
Mom.how_we_met()
