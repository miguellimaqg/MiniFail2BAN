import sqlite3

conexao = sqlite3.connect('seguranca.db')
cursor = conexao.cursor()

cursor.execute("SELECT * FROM ataques")
resultados = cursor.fetchall()

print("🛡️ --- RELATÓRIO DE INVASORES BLOQUEADOS --- 🛡️\n")

for linha in resultados:
    print(f"ID: {linha[0]}")
    print(f"IP do Atacante: {linha[1]}")
    print(f"Total de Tentativas: {linha[2]}")
    print(f"Data/Hora: {linha[3]}")
    print(f"Status no Firewall: {linha[4]}")
    print("-" * 40)

conexao.close()