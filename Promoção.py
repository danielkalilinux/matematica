# matematica
# ferramentas focada em  Matemática

print('''
 
██████╗░██████╗░░█████╗░███╗░░░███╗░█████╗░░█████╗░░█████╗░░█████╗░
██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██████╔╝██████╔╝██║░░██║██╔████╔██║██║░░██║██║░░╚═╝███████║██║░░██║
██╔═══╝░██╔══██╗██║░░██║██║╚██╔╝██║██║░░██║██║░░██╗██╔══██║██║░░██║
██║░░░░░██║░░██║╚█████╔╝██║░╚═╝░██║╚█████╔╝╚█████╔╝██║░░██║╚█████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝░╚════╝░
''')
preco = float(input('qual e a preco do produto? R$'))
promocao = float(input('digite a promocao: %'))


new = preco - (preco * promocao / 100)

print('A produto que custava R${:.2f}, na promocao com desconto de %{} vai custar R${:.2f}'.format(preco, promocao, new))

exit = input('obrigado....')
