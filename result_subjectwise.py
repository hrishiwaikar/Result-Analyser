# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 06:13:30 2016

@author: Jack
"""

filepath='becomp2012ledger.txt'
import matplotlib.pyplot as plt
import pygal
''' student class representing each student '''

class Student():
    student_count=0
    def __init__(self,serialno,insem_daa,insem_pmcd,insem_ssda,insem_pc,insem_dm,project_sem1,project_sem2_tw,project_sem2_oral,total,):
        self.serialno=serialno
        self.proj_1=project_sem1
        self.proj_2=project_sem2_tw
        self.proj_3=project_sem2_oral
        self.total=total
        self.project_total=self.proj_1+self.proj_2+self.proj_3
        self.pure_academic=self.total-self.project_total
        self.insem_daa=insem_daa
        self.insemdaacategory=self.getcategory(insem_daa)
        self.insem_pmcd=insem_pmcd
        self.insempmcdcategory=self.getcategory(insem_pmcd)
        self.insem_ssda=insem_ssda
        self.insemssdacategory=self.getcategory(insem_ssda)
        self.insem_pc=insem_pc
        self.insempccategory=self.getcategory(insem_pc)
        self.insem_dm=insem_dm
        self.insemdmcategory=self.getcategory(insem_dm)
        self.teacher_goodness=float(self.project_total)/self.pure_academic

    def getcategory(self,score):
        if score>=20:
            return 3
        elif score>=15:
            return 2
        elif score>=10:
            return 1
        else :
            return 0

students=[]
frequencies=[0,0,0,0]
daafrequencies=[0,0,0,0]
pmcdfrequencies=[0,0,0,0]
ssdafrequencies=[0,0,0,0]
pcfrequencies=[0,0,0,0]
dmfrequencies=[0,0,0,0]
below10=[0,0,0,0,0]
between10and15=[0,0,0,0,0]
between15and20=[0,0,0,0,0]
above20=[0,0,0,0,0]
insemdmlines=[]
with open(filepath) as file_object:
    content=file_object.read()

    projectlines=content.split('PROJECT                       TW 100 40              ')
    totallines=content.split('GRAND ')
    insem_daalines=content.split('DESIGN & ANALYSIS OF ALGO.    PP 100 40   ')
    insem_pmcdlines=content.split('PRIN. OF MODERN COML. DESIGN  PP 100 40   ')
    insem_dmlines=content.split('DATA MINING TECH. & APPL.     PP 100 40   ')
    insem_ssdalines=content.split('SMART SYSTEM DESIGN & APPL.   PP 100 40   ')
   # insem_pclines=content.split('PERVASIVE COMPUTING           PP 100 40   ')

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
        
        #daa insem
        insemdaaline=insem_daalines[i]
        insemdaascore=int(insemdaaline[:2])        
        #print insemdaascore
        
        #ssda insem
        insemssdaline=insem_ssdalines[i]
        insemssdascore=int(insemssdaline[:2])
        
        #pmcd insem
        insempmcdline=insem_pmcdlines[i]
        if insempmcdline[:2]=='  ':
            insempmcdscore=0
        else:
            insempmcdscore=int(insempmcdline[:2])
        
        #pcinsem
        #insempcline=insem_pclines[i]
        #print(i,insempcline[:2])
        #insempcscore=int(insempcline[:2])
        
        if 'PERVASIVE' in insempmcdline:
            insempclines=insempmcdline.split('PERVASIVE COMPUTING           PP 100 40   ')
            insempcline=insempclines[1]            
            insempcscore=int(insempcline[:2])
        else :
            insempcscore=0
        
        #print insempcscore
        
        #insem datamining
        
        if 'MINING' in insempmcdline:
            insemdmlines=insempmcdline.split('DATA MINING TECH. & APPL.     PP 100 40   ')
            insemdmline=insemdmlines[1]
            insemdmscore=int(insemdmline[:2])
        else:
            insemdmscore=0
            
        
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
        student=Student(i,insemdaascore,insempmcdscore,insemssdascore,insempcscore,insemdmscore,score1,score2,score3,grandtotal)
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
        '''  
        print "\nStudent no : "+str(students[i].serialno)
        print "Sem 1 Project marks  : "+str(students[i].proj_1)
        print "Sem 2 Project marks  : "+str(students[i].proj_2)
        print "Sem 3 Project marks  : "+str(students[i].proj_3)
        print "Total Project marks  : "+str(students[i].project_total)
        print "Non project total    : "+str(students[i].pure_academic)
        print "Total Academic score : "+str(students[i].total)
        print "Teacher goodness  score   : "+str(students[i].teacher_goodness)
        ''' 
       
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
        
       
        '''
        indaa=students[i].insem_daa
        inpmcd=students[i].insem_pmcd
        inssda=students[i].insem_ssda
        inpc=students[i].insem_pc
        '''
        daafrequencies[students[i].insemdaacategory]=daafrequencies[students[i].insemdaacategory]+1
        ssdafrequencies[students[i].insemssdacategory]=ssdafrequencies[students[i].insemssdacategory]+1
        pmcdfrequencies[students[i].insempmcdcategory]=pmcdfrequencies[students[i].insempmcdcategory]+1
        pcfrequencies[students[i].insempccategory]=pcfrequencies[students[i].insempccategory]+1
        dmfrequencies[students[i].insemdmcategory]=dmfrequencies[students[i].insemdmcategory]+1
        
        below10[1]=daafrequencies[0]
        below10[2]=ssdafrequencies[0]
        below10[0]=pmcdfrequencies[0]
        below10[3]=pcfrequencies[0]
        below10[4]=dmfrequencies[0]
        
        between10and15[1]=daafrequencies[1]
        between10and15[2]=ssdafrequencies[1]
        between10and15[0]=pmcdfrequencies[1]
        between10and15[3]=pcfrequencies[1]
        between10and15[4]=pcfrequencies[1]
        
        between15and20[1]=daafrequencies[2]
        between15and20[2]=ssdafrequencies[2]
        between15and20[0]=pmcdfrequencies[2]
        between15and20[3]=pcfrequencies[2]
        between15and20[4]=pcfrequencies[2]
        
        above20[1]=daafrequencies[3]
        above20[2]=ssdafrequencies[3]
        above20[0]=pmcdfrequencies[3]
        above20[3]=pcfrequencies[3]
        above20[4]=dmfrequencies[3]        
        
def project_scatterplot():
            
    plt.title("Project Marks Pattern Analysis",fontsize=20)
    plt.xlabel("Pure Academic Score",fontsize=13)
    plt.ylabel("Project Score",fontsize=13)
    print "Came in scatterplot()"
    #plt.show()
    plt.savefig('be2016resultplot.png',dpi=200)


def projecthistogram():
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
    
def insemhistogram_one():   
    print "In insemhistogram()"
    
    insemhisto=pygal.Bar()
    
    insemhisto.title="Insem Marks Distribution"
    insemhisto.x_labels=["Below 10","Between 10-15","Between 15-20","Above 20"]
    insemhisto.x_title=" Marks Categories"
    insemhisto.y_title="No. of students"
    
    insemhisto.add('DAA',daafrequencies)
    insemhisto.add('PMCD',pmcdfrequencies)
    insemhisto.add('SSDA',ssdafrequencies)
    insemhisto.add('PC',pcfrequencies)
    insemhisto.render_to_file('SubjectDistribution.sgv')

def insemhistogram_two():
    
    subjecthisto=pygal.Bar()
    subjecthisto.title="Subject Wise 2015 Insem Marks Distribution BarGraph"
    subjecthisto.x_labels=["PMCD","DAA","SSDA","PC","DM"]
    subjecthisto.x_title="Subjects"
    subjecthisto.y_title="No. of students"
    
    subjecthisto.add('Below 10',below10)
    subjecthisto.add('Between 10-15',between10and20)
    subjecthisto.add('Between 15-20',between15and20)
    subjecthisto.add('Above 20',above20)
    
    subjecthisto.render_to_file('InsemBarGraph.sgv')
    
    
analysis()
project_scatterplot()
projecthistogram()
insemhistogram_one()
insemhistogram_two()

print len(insem_dmlines)