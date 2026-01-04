from PyQt5.QtCore import QTime

win_x, win_y = 200, 100
win_width, win_height = 1000, 600

txt_hello = '¡Bienvenido al programa de detección del estado de salud!'
txt_next = 'Comenzar'

txt_instruction = ('Esta aplicación te permite usar el test de Ruffier para realizar un diagnóstico inicial de tu salud.\n'
                   'El test de Ruffier es un conjunto de ejercicios físicos diseñados para evaluar tu rendimiento cardíaco durante el esfuerzo físico.\n'
                   'El sujeto se acuesta en posición supina durante 5 minutos y se mide su pulso durante 15 segundos; \n'
                   'luego, en un lapso de 45 segundos, el sujeto realiza 30 sentadillas.\n'
                   'Al finalizar el ejercicio, el sujeto se acuesta y se le mide el pulso de nuevo durante los primeros 15 segundos\n'
                   'y después durante los últimos 15 segundos del primer minuto del periodo de recuperación.\n'
                   '¡Importante! Si te sientes mal durante la prueba (mareos,\n'
                   'zumbidos, falta de aire, etc.), detén la prueba y consulta a un médico.' )

txt_title = 'Salud'
txt_name = 'Ingresa tu nombre completo:'
txt_hintname = "Nombre completo"
txt_hintage = "0"
txt_test1 = 'Recuéstate boca arriba y tómate el pulso durante 15 segundos. Haz clic en el botón "Iniciar primera prueba" para iniciar el temporizador.\nEscribe el resultado en el campo correspondiente.'
txt_test2 = 'Realiza 30 sentadillas en 45 segundos. Para ello, haz clic en el botón "Iniciar sentadillas"\npara poner en marcha el contador de sentadillas.'
txt_test3 = 'Recuéstate boca arriba y tómate el pulso durante los primeros 15 segundos del minuto, y luego durante los últimos 15 segundos.\nPresiona el botón "Iniciar prueba final" para iniciar el temporizador.\nLos segundos que deben medirse se indican en verde y los minutos que no, en negro. Escribe los resultados en los campos correspondientes.'
txt_sendresults = 'Enviar los resultados'
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = 'Iniciar la primera prueba'
txt_starttest2 = 'Iniciar sentadillas'
txt_starttest3 = 'Iniciar la prueba final'
time = QTime(0, 0, 15)
txt_timer = time.toString("hh:mm:ss")
txt_age = 'Años cumplidos:'
txt_finalwin = 'Resultados'
txt_index = 'Índice de Ruffier: '
txt_workheart = 'Rendimiento cardíaco: '
txt_res1 = "bajo. ¡Consulta a tu médico de inmediato!"
txt_res2 = "satisfactorio. ¡Consulta a tu médico!"
txt_res3 = "promedio. Podría valer la pena consultar a tu médico."
txt_res4 = "por encima del promedio"
txt_res5 = "alto"
