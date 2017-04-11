filepath='becomp2012ledger.txt'
import matplotlib.pyplot as plt
import pygal
''' student class representing each student '''

class Student():
    student_count=0
    def __init__(self,serialno,project_sem1,project_sem2_tw,project_sem2_oral,total):
        self.serialno=serialno
        self.proj_1=project_sem1
        self.proj_2=project_sem2_tw
        self.proj_3=project_sem2_oral
        self.total=total
        self.project_total=self.proj_1+self.proj_2+self.proj_3
        self.pure_academic=self.total-self.project_total
        self.teacher_goodness=float(self.project_total)/self.pure_academic


students=[]
frequencies=[0,0,0,0]
        
with open(filepath) as file_object:
    content=file_object.read()

    projectlines=content.split('PROJECT                       TW 100 40              ')
    totallines=content.split('GRAND ')
    insemDaaLines=content.split('DESIGN & ANALYSIS OF ALGO.    PP 100 40   ')
    
    for i in range(1,len(projectlines)):
        projectline1=projectlines[i]
        projectlines2=projectline1.split('PROJECT                       TW  50 20              ')
        projectlines3=projectline1.split('PROJECT                       OR  50 20              ')
        grandtotallines=projectline1.split('GRAND TOTAL = ')
        
        #print projectlines2

        projectline2=projectlines2[1]
        projectline3=projectlines3[1]
        grandtotalline=grandtotallines[1]
        score2=int(projectline1[:2])
        score1=int(projectline2[:2])
        score3=int(projectline3[:2])
        if grandtotalline[0]=='-':
            grandtotal=0
        elif(grandtotalline[3]=='/'):
            grandtotal=int(grandtotalline[:3])
        else:
            grandtotal=int(grandtotalline[:4])
        
        #lastgrandtotal=grandtotal[3]
        ''' 
        print "Student "+str(i)+":"
        print "sem 1 project score :"+str(score1)
        print "sem 2 project score :"+str(score2)
        print "sem 3 project score :"+str(score3)
        print "grand total         :"+str(grandtotal)
        #print "lastgrandtotal      :"+lastgrandtotal
        '''
        ''' make a student object of this student and add it to students list'''
        student=Student(i,score1,score2,score3,grandtotal)
        students.append(student)

        
''' #code to print each student and his/her details        
for i in range(len(students)):
    print students[i].serialno
    print students[i].proj_1
    print students[i].proj_2
    print students[i].proj_3
    print students[i].total
    print "\n"
'''


def analysis():
    for i in range(len(students)):
            
      if(students[i].total!=0):
          
        print "\nStudent no : "+str(students[i].serialno)
        print "Sem 1 Project marks  : "+str(students[i].proj_1)
        print "Sem 2 Project marks  : "+str(students[i].proj_2)
        print "Sem 3 Project marks  : "+str(students[i].proj_3)
        print "Total Project marks  : "+str(students[i].project_total)
        print "Non project total    : "+str(students[i].pure_academic)
        print "Total Academic score : "+str(students[i].total)
        print "Teacher goodness  score   : "+str(students[i].teacher_goodness)
         
       
        if students[i].teacher_goodness<0.19 :
            frequencies[0]=frequencies[0]+1
            #print "\nUnlucky student : got project marks worse than his academic. Bad teacher!"      
        elif students[i].teacher_goodness>0.19 and students[i].teacher_goodness<0.21 :
            frequencies[1]=frequencies[1]+1
            # print "\nNormal Luck : got project marks relative to academic performance. Fine teacher!"
        elif students[i].teacher_goodness>0.21 and students[i].teacher_goodness<0.23 :
            frequencies[2]=frequencies[2]+1
            # print "\nLucky student : got project marks better than academic performance. Good teacher!"
        elif students[i].teacher_goodness>0.23 :
            frequencies[3]=frequencies[3]+1
    
        pureacad=students[i].pure_academic
        project=students[i].project_total
        plt.scatter(pureacad,project,c=project,cmap=plt.cm.coolwarm,edgecolor='none',s=8)
        #plt.scatter(pureacad,project,c=project,cmap=plt.cm.Blues,s=40)
       
       
        
def scatterplot():
    
        
    plt.title("Project Marks Pattern Analysis",fontsize=20)
    plt.xlabel("Pure Academic Score",fontsize=13)
    plt.ylabel("Project Score",fontsize=13)
    print "Came in scatterplot()"
    #plt.show()
    plt.savefig('be2016resultplot.png',dpi=200)


def histogram():
    print "Came in histogram()"
    histo=pygal.Bar()
    
    #we build a histogram of frequencies of students belonging to c3 categories
    #unlucky , normal , lucky
    
    histo.title="Project Marks Luck Analysis"
    histo.x_labels=["Very Unlucky","Normal luck","Lucky","Very Lucky"]
    histo.x_title="Students categorized based on luck of getting good project score"
    histo.y_title="Number of Students"
    
    histo.add('BE2016',frequencies)
    histo.render_to_file('ProjectScoreAnalysis.sgv')
    
analysis()
scatterplot()
histogram()

