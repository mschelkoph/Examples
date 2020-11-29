using System;
using System.IO;
using System.Collections.Generic;
using System.Text;

namespace HealthRecords
{
    class client
    {
        //data 
        private string fname;
        private string mInitial;
        private string lname;
        private int age;
        private string gender;
        private int Hfeet;
        private int Hinches;
        private double weight;
        private int birthyear;
        private int currentyear;






        public client(string fname, string mInitial, string lname, string g, int Hfeet, int Hinches,

            double w, int birthyear, int curryear)
        {
            //to refer to the instance variable use this 
            this.fname = fname;
            this.mInitial = mInitial;
            this.lname = lname;
            gender = g;
            this.Hfeet = Hfeet;
            this.Hinches = Hinches;
            this.weight = w;
            this.birthyear = birthyear;
            currentyear = curryear;

        }

        public client()
        {
            fname = "default";
            mInitial = "default";
            lname = "default";
            gender = "default";
            Hfeet = 0;
            Hinches = 0;
            weight = 0;
            birthyear = 0;
            currentyear = 0;
        }

        public string getFname()
        {
            return fname;
        }
        public void setFname(string x)
        {
            fname = x;
        }

        public string getmInitial()
        {
            return mInitial;
        }
        public void setmInitial(string x)
        {
            mInitial = x;
        }

        public string getLname()
        {
            return lname;

        }
        public void setLname(string x)
        {
            lname = x;
        }
        
        public string getGender()
        {
            return gender;
        }
        public void setGender(string x)
        {
            gender = x;
        }

        public int getHfeet()
        {
            return Hfeet;
        }
        public void setHfeet(int x)
        {
            Hfeet = x;
        }

        public int getHinches()
        {
            return Hinches;
        }
        public void setHinches(int x)
        {
            Hinches = x;
        }

        public double getWeight()
        {
            return weight;
        }
        public void setWeight(double x)
        {
            weight = x;
        }
        public int getBirthYear()
        {
            return birthyear;
        }
        public void setBirthYear(int x)
        {
            birthyear = x;
        }

        public int getAge()
        {
            return age;
        }
        public void setAge(int x)
        {
            age = x;
        }

        public int getCurrentYear()
        {
            return currentyear;
        }
        public void setcurrentyear(int x)
        {
            currentyear = x;
        }

        private double calculateBMI()
        {
            int heightInInches = (getHfeet() * 12) + getHinches();
            double bmi = 0.0;
            bmi = (weight / Math.Pow(heightInInches, 2) * 703);
            return bmi;
        }
        public void DisplayInfo()
        {
            double bmi = calculateBMI();
            using (StreamWriter writer = new StreamWriter("C:\\Users\\Mark PC\\Desktop\\Assignment 2.txt", true))
            {
                writer.WriteLine($"Health Record For: {fname} {mInitial} {lname}, Age: {age}");
                writer.WriteLine($"Gender: {gender}, height: {Hfeet} feet {Hinches} inches, (in inches only: {(getHfeet() * 12) + getHinches()}), weight:{weight}");
                writer.WriteLine($"BMI: {calculateBMI() }");
                writer.WriteLine("\n");
            }

            //everything else ...you need to print about the client  

            

        }



    }//class 


} //namespace
