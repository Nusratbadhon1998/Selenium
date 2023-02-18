from helium import *
from bs4 import BeautifulSoup as bs

class Web:
    
    #log = CustomLogger.log("mongo.log")
    
    def __init__(self,url, searchString):
        try:
        
            self.url= url+searchString
            
        except Exception as e:
            
            print("mm")
        else:
            self.browser= start_chrome(self.url,headless=True)
            self.html= self.browser.page_source
            self.soup= bs(self.html,'html.parser')
            self.course= (self.soup.find_all("div",{"class": "Course_course-card__f7WLr Course_card__rBLhD card"}))

        """finally:
            self.filename = searchString + ".csv"
            fw = open(self.filename, "w")
            headers = "CourseName, Customer Name, Rating, Heading, Comment \n"
            fw.write(headers)
            self.reviews = []"""
    def all(self):
        self.courses=[]
        for i in self.course :
            if (i.div.a['href']) not in self.courses:
                self.courses.append(i.div.a['href'])
                
        for j in self.courses:
            productLink = 'https://ineuron.ai'+ j
            self.browser= start_chrome(productLink,headless=True)
            self.prodRes= self.browser.page_source
            prod_html = bs(self.prodRes, "html.parser")
            #title
            self.title=  prod_html.find('h3',{'class':'Hero_course-title__4JX81'}).text
            #description
            self.des = prod_html.find('div', {'class': "Hero_course-desc__lcACM"}).text
            #module
            learn=prod_html.find('div', {'class': "CourseLearning_card__0SWov card"})
            modules= learn.find_all('li')
            #mo
            mm=[]
            for module in modules:
                mm.append(module)
                print(module.text,end=',')
            print(" ")
            #requirements
            req= prod_html.find('div', {'class': "CourseRequirement_card__lKmHf requirements card"})
            rq=  req.find_all('li')
            print("The requirements are: ")
            rr=[]
            for r in rq:
                rr.append(r)
                print(r.text,end=',')
            print(" ")
            ccur= prod_html.find_all('div', {'class': "CurriculumAndProjects_curriculum-accordion__fI8wj CurriculumAndProjects_card__rF6YN card"})
            print("course curriculums are: ")
            for cc in range(len(ccur)):
                d= f"curriculumref{cc}"
                x=ccur[cc].find("ul",{'id':d})
                ccc=[]
                for o in x.find_all("li"):
                    ccc.append((ccur[cc].div.text,o.text))  
        
                print(f"{cc+1}.{ccur[cc].div.text} : {ccc}")
            print(" ")
            det= prod_html.find('div', {'class': "CoursePrice_price-card__NLBzN CoursePrice_card__cnXiw card"})
            price= prod_html.find('div', {'class':"CoursePrice_price__YLG0U"})  

            #privceeee
            p=price.div.div.text  
            print("The course price is: ")
            print(price.div.div.text)

            #detailssssss

            d=det.find("div",{"class":"CoursePrice_timings__ntCCV"})   
            print("Class Details: ")
            y=[]
            for k in d.find_all("div",{"class":"CoursePrice_time__p0s9t"}):
                y.append(k.text)
                
            x=[]
            for k in d.find_all("strong"):
                x.append(i.text)
            dd=[] #detailssss
            for k in range(len(x)):
                dd.append((x[k],y[k]))
                print(x[k]+' '+ y[k])
            print(" ")
            
            det= prod_html.find('div', {'class': "CoursePrice_price-card__NLBzN CoursePrice_card__cnXiw card"})
            d1=det.find("div",{"class":"CoursePrice_course-features__IBpSY"})
            for z in d1.find_all("li"):
                print(z.text,end=',')
            print(" ")
            
            instruction=prod_html.find_all('div', {'class': "InstructorDetails_left__nVSdv"})
            for ins in instruction:
                try: 
                    print(ins.h5.text)
                    print(ins.find("p").text)
                    li= ins.div.find_all("a")
                    for l in li:
                        print(l['href'])
                    print(" ")
                except:
                    pass

    

    

    

        
    def all_course_name(self):
        self.courses=[]
        try:
            for i in self.course :
                if i.div.h5.text not in self.courses:
                    self.courses.append(i.div.h5.text)
        except Exception as e:
            print(e)
        else:
            print(self.courses)
            return (self.courses)
            

    def all_course_link(self,):
        self.links=[]
        for i in self.course :
            if (i.div.a['href']) not in self.links:
                 self.links.append('https://ineuron.ai'+ i.div.a['href'])
        
        #print(self.links)
        return (self.links)

    def course_html(self,link):
        self.link=link
        #links= self.all_course_link()
        try:
                course_browser= start_chrome(self.link,headless=True)
                course_html= course_browser.page_source
                course_soup= bs(course_html,'html.parser')
        except Exception as e:
            print(e)
        else:
            return course_soup



    """def title(self):
        links= self.all_course_link()
        try:
            
                course_soup=self.course_html(l)
                title=  course_soup.find_all('h3',{'class':'Hero_course-title__4JX81'})
                print(f"The course title is: ")
                for t in title:
                    print(t.text)
                
                
        except Exception as e:
            print(e)
        else:
            pass"""

    def course_description(self):
        links= self.all_course_link()
        try:
            for l in links:
                course_soup=self.course_html(l)
                self.des = course_soup.find('div', {'class': "Hero_course-desc__lcACM"}).text
                print("This is the course description:")
                print(self.des)
        except Exception as e:
            print(e)
        else:
            self.des

    def module(self):
        links= self.all_course_link()
        try:
            for l in links:
                course_soup=self.course_html(l)
                learn= course_soup.find('div', {'class': "CourseLearning_card__0SWov card"})
                print("Course Modules are:")
                modules= learn.find_all('li')
                self.mm=[]
                for m in modules:
                    self.mm.append(m)
                    print(m.text,end=',')
                print(" ")
                
        except Exception as e:
            print(e)
        else:
            self.mm

    def requirements(self):
        links= self.all_course_link()
        try:
            for l in links:
                course_soup=self.course_html(l)
                req= course_soup.find('div', {'class': "CourseRequirement_card__lKmHf requirements card"})
                rq=  req.find_all('li')
                print("The requirements are: ")
                self.require= []
                for r in rq:
                    self.require.aapend(r)
                    print(r.text,end=',')
                print(" ")

        except Exception as e:
            print(e)
        else:
            return self.require

    def curriculum(self):
        links= self.all_course_link()
        try:
            for l in links:
                course_soup=self.course_html(l)
                ccur= course_soup.find_all('div', {'class': "CurriculumAndProjects_curriculum-accordion__fI8wj CurriculumAndProjects_card__rF6YN card"})
                print("course curriculums are: ")
                
                for cc in range(len(ccur)):
                    self.ctitle=[]
                    self.ctitle.append(ccur[cc].div.text)
                    print(ccur[cc].div.text)
                    d= f"curriculumref{cc}"
                    x=ccur[cc].find("ul",{'id':d})
                    self.ccurriculumn=[]
                    for o in x.find_all("li"):
                        self.ccurriculumn.append(o.text)
                        print(o.text)  
                
                    
                    print(" ")
            self.all=[]
            for k in range(len(self.ctitle)):
                    print(self.title[k]+' '+ self.ccurriculumn[k])
                    self.all.append(self.title[k]+' '+ self.ccurriculumn[k])

        except Exception as e:
            print(e)

    def course_price(self):
        links= self.all_course_link()
        try:
            for l in links:
                course_soup=self.course_html(l)
                price= course_soup.find('div', {'class':"CoursePrice_price__YLG0U"})    
                print("The course price is: ")
                print(price.div.div.text)
        except Exception as e:
            print(e)
    def class_details(self):
        links= self.all_course_link()
        try:
            for l in links:
                course_soup=self.course_html(l)
                det= course_soup.find('div', {'class': "CoursePrice_price-card__NLBzN CoursePrice_card__cnXiw card"})
                d=det.find("div",{"class":"CoursePrice_timings__ntCCV"})   
                print("Class Details: ")
                y=[]
                for k in d.find_all("div",{"class":"CoursePrice_time__p0s9t"}):
                    y.append(k.text)
                    
                x=[]
                for k in d.find_all("strong"):
                    x.append(k.text)
                    
                for k in range(len(x)):
                    print(x[k]+' '+ y[k])
                print(" ")
        except Exception as e:
            print(e)

    def instruction_details(self):
        links= self.all_course_link()
        try:
            for l in links:
                course_soup=self.course_html(l)
                instruction=course_soup.find_all('div', {'class': "InstructorDetails_left__nVSdv"})
                for ins in instruction:
                    try: 
                        print(ins.h5.text)
                        print(ins.find("p").text)
                        li= ins.div.find_all("a")
                        for l in li:
                            print(l['href'])
                        print(" ")
                    except:
                        pass
        except Exception as e:
            print(e)




w= Web("https://ineuron.ai/category/","DATA-SCIENCE")

w.all_course_name()