import os
#Make the console text a green color
os.system('color a')
#Sets up the base file
prework = '\\documentclass[11pt,letterpaper,roman]{moderncv}\n'
prework += '\\moderncvstyle{banking}'
prework += '\\moderncvcolor{blue}\n'
prework += '\\nopagenumbers{}\n'
prework += '\\usepackage[utf8]{inputenc}\n'
prework += '\\usepackage{fontawesome}\n'
prework += '\\usepackage{fontspec}\n'
prework += '\\usepackage{tabularx}\n'
prework += '\\usepackage{ragged2e}\n'
prework += '\\usepackage[scale=0.8]{geometry}\n'
prework += '\\usepackage{multicol}\n'
prework += '\\usepackage{import}\n'
first_name = input('What is your first name?\n')
last_name = input('What is your last name?\n')
prework += '\\name{'
prework += f'{first_name}'
prework += '}{'
prework += f'{last_name}'
prework += '}\n'
#Basic Information
prework += '\\address{'
address = input('What is your address? Street, City, ST 00000\n')
prework += f'{address}'
prework += '}{}{}\n'

prework += '\\newcommand*{\\customcventry}[7][.25em]{\n'
prework += '\t\\begin{tabular}{@{}l}\n'
prework += '\t\t{\\bfseries #4}\n'
prework += '\t\\end{tabular}\n'
prework += '\t\\hfill\n'
prework += '\t\\begin{tabular}{l@{}}\n'
prework += '\t\t{\\bfseries #5}\n'
prework += '\t\\end{tabular} \\\\\n'
prework += '\t\\begin{tabular}{@{}l}\n'
prework += '\t\t{\\itshape #3}\n'
prework += '\t\\end{tabular}\n'
prework += '\t\\hfill\n'
prework += '\t\\begin{tabular}{l@{}}\n'
prework += '\t\t{\\itshape #2}\n'
prework += '\t\\end{tabular}\n'
prework += '\t\\ifx&#7&%\n'
prework += '\t\\else{\\\\%\n'
prework += '\t\t\\begin{minipage}{\\maincolumnwidth}%\n'
prework += '\t\t\t\\small#7%\n'
prework += '\t\t\\end{minipage}}\\fi%\n'
prework += '\t\\par\\addvspace{#1}}\n'
prework += '\\newcommand*{\\customcvproject}[4][.25em]{\n'
prework += '\t\\begin{tabular}{@{}l}\n'
prework += '\t\t{\\bfseries #2}\n'
prework += '\t\\end{tabular}\n'
prework += '\t\\hfill% move it to the right\n'
prework += '\t\\begin{tabular}{l@{}}\n'
prework += '\t\t{\\itshape #3}\n'
prework += '\t\\end{tabular}\n'
prework += '\t\\ifx&#4&%\n'
prework += '\t\\else{\\\\%\n'
prework += '\t\t\\begin{minipage}{\\maincolumnwidth}%\n'
prework += '\t\t\t\\small#4%\n'
prework += '\t\t\\end{minipage}}\\fi%\n'
prework += '\t\\par\\addvspace{#1}}\n'
prework += '\\setlength{\\tabcolsep}{12pt}\n'
latex = prework
latex += '\\begin{document}\n'
latex += '\\makecvtitle\n'
latex += '\\vspace*{-18mm}\n'
latex += '\\begin{center}\n'
latex += '\\begin{tabular}{ c c c c }\n'
latex += '\t\\faGlobe\\enspace \\href{'
linx = input('What is your website, email, LinkedIn, and phone? (website email linkedin (###)-###-####)\n')
my_site = linx.split()[0]
email = linx.split()[1]
linked_in = linx.split()[2]
phone = linx.split()[3]

#Contact Information
latex += f'{my_site}'
latex += '}{'
latex += f'{my_site}'
latex += '} & \\faEnvelopeO\\enspace \\href{'
latex += f'{email}'
latex += '}{'
latex += f'{email}'
latex += '} & \\faGithub\\enspace '
latex += f'{linked_in}'
latex += f' & \\faMobile\\enspace {phone}\\\\\n'

latex += '\\end{tabular}\n'
latex += '\\end{center}\n'
latex += '\\section{EDUCATION}\n'

#Education
ex_grad = input('What is your expected graduation? (Month YYYY)\n')
degree = input('What degree are you pursuing?\n')
gpa = input('What is your GPA?\n')
college = input('What university do you attend?\n')
col_city = input('What is the location of the university? (City, ST)\n')
latex += '{\\customcventry{Expected Graduation: '
latex += f'{ex_grad}'
latex += '}{'
latex += f'{degree}'
latex += f' GPA: {gpa}'
latex += '}{'
latex += f'{college}'
latex += '}{'
latex += f'{col_city}'
latex += '}{}{}}\n'

#Experience
latex += '\\section{EXPERIENCE}\n'
print('For this next step, leave the entry field blank to stop adding items and move to next field. Enter each entry individually.')
job = '1'
while (job != ''):
    job = input('What job/internship have you participated in? (Job Position ex. Engineer)\n')
    if job == '':
        break
job_time = input('When was your period of work? (Month YYYY - Month YYYY)\n')
company = input('What company did you work for?\n')
job_loc = input('Where did you work?\n')
latex += '{\\customcventry{'
latex += f'{job_time}'
latex += '}{'
latex += f'{job}'
latex += '}{'
latex += f'{company}'
latex += '}{'
latex += f'{job_loc}'
latex += '}{}\n'
desc_det = input('Do you want to add a short description? (Y/N)\n')
if desc_det.upper() != 'Y':
    pass
elif desc_det.upper() == 'Y':
    description = '1'
latex += '{\\begin{itemize}\n'
while (description != ''):
    description = input('Please write a short bullet point description. If you would like to add more than one point, fill this entry again when prompted. Otherwise, leave it blank.\n')
    if description == '':
        break
    latex += f'\t\\item {description}\n'
    latex += '\\end{itemize}\n'
    latex += '}\n'

#Projects
latex += '\\section{PROJECTS}\n'
proj = '1'
print('For this next step, leave the entry field blank to stop adding items and move to next field. Enter each entry individually.')
while (proj != ''):
    proj = input('What project have you worked on?\n')
    if proj == '':
        break
    proj_date = input('When did you work on this project? (Month YYYY - Month YYYY)\n')
    latex += '{\\customcvproject{'
    latex += f'{proj}'
    latex += '}{'
    latex += f'{proj_date}'
    latex += '}\n'
    proj_desc = '1'
    latex += '{\\begin{itemize}\n'
    while (proj_desc != ''):
        proj_desc = input('Please write a short bullet point description. If you would like to add more than one point, fill this entry again when prompted. Otherwise, leave it blank.\n')
        if proj_desc == '':
            break
        latex += f'\t\\item {proj_desc}\n'
        latex += '\\end{itemize}\n'
        latex += '}\n'
        latex += '}\n'

#Additional
print('This next section is for clubs, relevant coursework, hobbies, or other additional information.\n')
latex += '\\section{AWARDS}\n'
latex += '\\begin{minipage}{\\maincolumnwidth}%\n'
latex += '\t\\small{\n'
latex += '\t\t\t\\begin{itemize}\n'
addi = '1'
while (addi != ''):
    addi = input('What additional club, hobby, relevant course, or additional info do you want to include?\n')
    if addi == '':
        break
    latex += f'\t\t\t\t\\item {addi}\n'
    latex += '\t\t\t\\end{itemize}}%\n'
    latex += '\\end{minipage}%\n'
    latex += '}\n'

latex += '\\end{document}'
#Reformats string to txt
print(latex)
#Exports latex file
f = open("resume.tex","w")
f.write(latex)
f.close()