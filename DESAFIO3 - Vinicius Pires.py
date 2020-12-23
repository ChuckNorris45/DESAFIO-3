import csv

#-----variáveis para calculo do cr dos alunos-----
ch_total = 0 #carga horária total de uma mesma pessoa.
mat = "100" #matrícula
notaxch = 0  # valor da nota vezes a carga horaria de cada disciplina.


#-----variáveis para calculo da média das turmas-----
notaxch_4 = 0
ch_total_4 = 0

notaxch_56 = 0
ch_total_56 = 0

notaxch_21 = 0
ch_total_21 = 0

notaxch_103 = 0
ch_total_103 = 0

notaxch_31 = 0
ch_total_31 = 0


#-----calculo dos CRs dos alunos-----
with open("csv.txt", encoding='utf-8') as teste: ###---arquivo csv a ser lido.---
  print('------- O CR dos alunos é: --------')
  reader = csv.reader(teste)  #leitura do arquivo
  for row in reader:
        if row[0] != "MATRICULA":  # a primeira linha é o cabeçario, então é pulada.
              if row[0] == mat: #matrícula

                  notaxch += int(row[3])*int(row[4])
                  ch_total += (int(row[4]))

              elif row[0] == "":     # serve apenas para o último item da lista          
                  print('%.2f' % (notaxch/ch_total))
                  

                  
              else:
                  print(mat, ' - ', '%.2f' % (notaxch/ch_total))
                  mat = row[0]
                  notaxch += int(row[3])*int(row[4])
                  ch_total += (int(row[4]))
print('-----------------------------------')


#-----calculo dos CRs dos alunos-----
with open("csv.txt", encoding='utf-8') as teste:  #cr das turmas

  reader = csv.reader(teste)  #leitura do arquivo
  for row in reader:
       if row[0] != "MATRICULA": #A primeira linha é o cabeçario então pulamos aqui também.
             if row[2] == "4": # turma 4
                   notaxch_4 += int(row[3])*int(row[4])
                   ch_total_4 += int(row[4])

             elif row[2] == "21": #turma 21
                   notaxch_21 += int(row[3])*int(row[4])
                   ch_total_21 += int(row[4])

             elif row[2] == "31": #turma 31
                   notaxch_31 += int(row[3])*int(row[4])
                   ch_total_31 += int(row[4])

             elif row[2] == "56":  # turma 56
                   notaxch_56 += int(row[3])*int(row[4])
                   ch_total_56 += int(row[4])

             elif row[2] == "103":  #turma 103
                   notaxch_103 += int(row[3])*int(row[4])
                   ch_total_103 += int(row[4])

              
print("\n", "----- Média de CR dos cursos ------")
print('4   - ', "%.2f" % (notaxch_4/ch_total_4))
print('21  - ', "%.2f" % (notaxch_21/ch_total_21))
print('31  - ', "%.2f" % (notaxch_31/ch_total_31))
print('56  - ', "%.2f" % (notaxch_56/ch_total_56))
print('103 - ', "%.2f" % (notaxch_103/ch_total_103))
print('-----------------------------------')



              
          
         

    
