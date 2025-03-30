dictionary = {}

def main(stroka: str):
    text = ''.join(stroka.split('\n')).strip('done.>>').replace(' ', '')
    text = text.split('@')[1:]
    text = [i.rstrip(';done.donew') for i in text]
    for stroka in text:
        stroka = stroka.replace("'", "")
        key, value = stroka.split(':')
        value = value.strip('#').strip('()').split(';')
        dictionary[key] = value
    return dictionary


dannie = "<< do new @'avea' : #('isve_803'; 'orisor' ; 'lemaat' ); done. do new\n@'dimaon_947' : #( 'istele'; 'dior' ); done. do new @'geceso_976'\n:#('quso_200' ; 'ratian_166' ); done. do new @'diorve_14' :#( 'tevere'\n; 'onte_700' ); done.>>"

print(main(dannie))