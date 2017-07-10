from appJar import gui
import sqlite3

'''
CREATE TABLE USUARIO(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, EMAIL TEXT NOT NULL, TYPE TEXT NOT NULL, DEPARTMENT TEXT NOT NULL, PROGRAM TEXT NOT NULL, CAMPUS TEXT NOT NULL, PERIODICITY TEXT NOT NULL);
CREATE TABLE RSS(ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, TYPE TEXT NOT NULL, KNOWLEDGE_AREA TEXT NOT NULl, DATABASE_URL TEXT NOT NULL);
CREATE TABLE RSS_DB(ID INT PRIMARY KEY, BDD TEXT NOT NULL,URL TEXT NOT NULL, FOREIGN KEY(BDD) REFERENCES RSS(ID))
CREATE TABLE USUARIO_RSS(USUARIO_ID INT , RSS_ID INT, FOREIGN KEY(USUARIO_ID) REFERENCES USUARIO(ID));
'''

def reOrganize(var):
    print app.getOptionBox(var)

def generate_reports():
    print "Generando Reportes"
    
def menuPress(mn):
    if mn == "Generar Reportes":
        generate_reports()
    else:
        conn.close()
        app.stop()
    
def usuarioPress(mn):
    values = [app.getEntry('usuario_name'), app.getEntry('usuario_email'), app.getOptionBox('Tipo'), app.getOptionBox('Campus'), app.getOptionBox('Departamento'), app.getOptionBox('Programa'), app.getOptionBox('Periodicidad')]
    if mn == "Guardar":
        c.execute('INSERT INTO USUARIO(NAME, EMAIL, TYPE, DEPARTMENT, PROGRAM, CAMPUS, PERIODICITY) VALUES (?, ?, ?, ?, ?, ?, ?)', values)
        conn.commit()
        print "Guardando Usuario"
    elif mn == "Editar":
        values.append('1')
        c.execute('UPDATE USUARIO NAME=?, EMAIL=?, TYPE=?, DEPARTMENT=?, PROGRAM =?, CAMPUS=?, PERIODICY=? WHERE ID=?', values)
        conn.commit()
        print "Editando Usuario"
    else:
        id_usuario=1
        c.execute('DELETE FROM USUARIO WHERE ID=?', id_usuario)
        conn.commit()
        print "Eliminando Usuario"
    
def rssPress(mn):

    if mn == "Guardar":
        print "Guardando RSS"
    else:
        print "Eliminando RSS"
    
conn = sqlite3.connect('example.db')
c = conn.cursor()

app = gui('Portal de Informacion')

app.addMenuList('File', ['Generar Reportes','-', 'Close'], menuPress)
app.addMenuList('Usuario', ['Guardar', 'Editar', 'Eliminar'], usuarioPress)
app.addMenuList('RSS', ['Guardar', 'Eliminar'], rssPress)

app.addLabel('usuarios', 'Usuarios', 0, 0, 4)
app.setLabelBg('usuarios', 'red')
app.addLabel('usuario_name', 'Nombre de Usuario', 1, 0, 1)
app.addEntry('usuario_name', 1, 1, 1)
app.addLabel('usuario_email', 'Correo', 1, 2, 1)
app.addEntry('usuario_email', 1, 3, 1)
app.addLabelOptionBox('Tipo', ['Maestro', 'Estudiante', 'Administrativo'], 2, 0, 2)
app.addLabelOptionBox('Campus', ['Mexicali', 'Tijuana', 'Ensenada'], 2, 2, 2)
app.addLabelOptionBox('Departamento', ['CIENCIAS SOCIALES', 'DERECHO', 'PSICOLOGIA', 'INGENIERIA', 'ADMINISTRACION Y NEGOCIO', 'ADMINISTRATIVO', 'SOCIEDAD', 'TECNOLOGIA', 'PROPIEDAD INTELECTUAL', 'CULTURA', 'INVESTIGACION'], 3, 0, 2)
app.addLabelOptionBox('Programa', ['LICENCIATURA EN CONTADOR PUBLICO', 'DOCTORADO EN ADMINISTRACION', 'DOCTADORADO EN INGENIERIA', 'DOCTADORADO EN EDUCACION', 'DOCTORADO EN PSICOLOGIA', 'INGENIERIA EN CIENCIAS COMPUTACIONALES', 'INGENIERIA EN CIBERNETICA ELECTRONICA', 'INGENIERIA EN DISENO GRAFICO DIGITAL', 'INGENIERIA EN ENERGIAS RENOVABLES', 'INGENIERIA INDUSTRIAL', 'INGENIERIA MECANICA', 'INGENIERIA MECATRONICA', 'INGENIERIA DE SOFTWARE', 'LICENCIATURA EN ADMINISTRACION DE EMPRESAS', 'LICENCIATURA EN ADMINISTRACION DE MERCADOTECNIA', 'LICENCIATURA EN ADMINISTRACION DE NEGOCIOS', 'LICENCIATURA EN DERECHO', 'LICENCIATURA EN DISENO GRAFICO', 'PSICOLOGIA INFANTIL', 'LICENCIATURA EN NEGOCIOS INTERNACINALES', 'PSICOLOGIA CLINICA', 'PSICOLOGIA EDUCATIVA', 'PSICOLOGIA ORGANIZACIONAL', 'PREPARATORIA'], 3, 2, 2)
app.setOptionBoxChangeFunction('Tipo', reOrganize)
app.addLabel('id_rss', 'ID RSS', 4, 0, 1)
app.addEntry('id_rss', 4, 2, 3)
app.addLabelOptionBox('Periodicidad', ['1 Semana', '2 Semanas', '1 mes', '2 meses', '3 meses'], 5, 0, 4)

app.addLabel('rss_bd', 'RSSs', 7, 0, 4)
app.setLabelBg('rss_bd', 'blue')
app.addLabel('rss_name', 'Nombre RSS', 8, 0, 1)
app.addEntry('rss_name', 8, 1,1)
app.addLabelOptionBox('Area_Conocimiento', ['DERECHO', 'PSICOLOGIA', 'EDUCACION', 'FILOSOFIA', 'CS. SOCIALES', 'INGENIERIA', 'CS. COMPUTACIONALES', 'ADMINISTRACION Y NEGOCIOS', 'OTROS'], 8, 2, 2)

app.go()
