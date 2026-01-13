def testando_erro():
    try:
        nome = input("Digite nome: ")
        nome = int(nome)
        if type(nome) != str:
            raise ValueError

    except StopAsyncIteration:
        return "GOD"
    
    except ValueError:
        return "OMG"
    
    except:
        return "Outro erro!"
    
a = testando_erro

print(a())