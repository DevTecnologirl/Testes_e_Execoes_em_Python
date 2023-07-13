
data_hora = datetime.strptime(linha, '%Y-%m-%d %H:%M:%S\n')
try:
        data_hora = datetime.strptime(linha, '%Y-%m-%d %H:%M:%S\n')
        data_hora_br = data_hora.strftime('%d/%m/%Y %H:%M\n')
        registros_br.write(data_hora_br)
finally:
        registros_ansi.close()
        registros_br.close()