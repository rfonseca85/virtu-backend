from docxtpl import DocxTemplate

doc = DocxTemplate("src/virtu_hunter/templates/resume_template1.docx")
context = { 'name' : "Ana Gabriela", 
           'lastName' : "Lopes Fonseca",
            'title': "Manager",
            'contact': {
                'city': 'Toronto',
                'province': 'ON',
                'phone': '647-222-2222',
                'email': 'anagabilopes@gmail.com',
                'linkedin': 'linkedin.com/in/anagabilopes'
                },
             'summary': 'I am a software developer with 5 years of experience in developing software', 
             'experiences': [
                  {
                      'companyName': 'Company 1',
                      'title': 'Software Developer',
                      'startDate': '2019',
                      'endDate': '2021',
                      'description': [{'point': 'Developed software'}, {'point': 'Developed software'}]
                  },
                    {
                        'companyName': 'Company 2',
                        'title': 'Software Developer',
                        'startDate': '2017',
                        'endDate': '2019',
                        'description': [{'point': 'Developed software'}, {'point': 'Developed software'}]
                    },
                    {
                        'companyName': 'Company 3',
                        'title': 'Software Developer',
                        'startDate': '2015',
                        'endDate': '2017',
                        'description': [{'point': 'Developed software'}, {'point': 'Developed software'}]
                    }
             ], 
            'skills': [
                {
                    'category': 'Programming Languages',
                    'description': 'Python, Java, C#'
                },
                {
                    'category': 'Frameworks',
                    'description': 'Django, Flask, Spring'
                },
                {
                    'category': 'Databases',
                    'description': 'MySQL, PostgreSQL, MongoDB'
                },
                {
                    'category': 'Tools',
                    'description': 'Git, Docker, Jenkins'
                }
            ],
             'education': [
                 {
                     'degree': 'Computer Science',
                     'school': 'University of Toronto',
                     'startDate': '2011',
                     'endDate': '2015'
                 }
             ],    
            }
doc.render(context)
doc.save("generated_doc.docx")