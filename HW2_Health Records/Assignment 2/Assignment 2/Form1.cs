using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Newtonsoft.Json;
using HealthRecords;

namespace Assignment_2
{
    public partial class Form1 : Form
    {
        Random randNum = new Random();
        string gender = "";
        int count = 0;
        static DateTime time = DateTime.Now;
        client[] People = new client[5];

        public Form1()
        {
            InitializeComponent();

            label10.Text = time.ToString();

            for(int i = 0; i < 5; i++)
            {
                People[i] = new client();
            }
        }

        private void Submit_Click(object sender, EventArgs e)
        {
            if(String.IsNullOrEmpty(fName.Text)|| String.IsNullOrEmpty(mInitial.Text) || String.IsNullOrEmpty(lName.Text) || String.IsNullOrEmpty(Hfeet.Text) || String.IsNullOrEmpty(Hinches.Text) ||
                                    String.IsNullOrEmpty(Weight.Text) || String.IsNullOrEmpty(currYear.Text))
            {
                MessageBox.Show("You must fill in all text boxes!");
            }
            else
            {
                if (genderM.Checked == false && genderF.Checked == false)
                {
                    MessageBox.Show("You must choose a gender!");
                }
                else
                {
                    if (genderM.Checked == true)
                    {
                        gender = "M";
                    }
                    else if (genderF.Checked == true)
                    {
                        gender = "F";
                    }

                    People[count].setFname(fName.Text);
                    People[count].setmInitial(mInitial.Text);
                    People[count].setLname(lName.Text);
                    People[count].setGender(gender);
                    People[count].setHfeet(int.Parse(Hfeet.Text));
                    People[count].setHinches(int.Parse(Hinches.Text));
                    People[count].setWeight(double.Parse(Weight.Text));
                    People[count].setcurrentyear(int.Parse(currYear.Text));
                    People[count].setBirthYear(randNum.Next(80) + 1930);
                    People[count].setAge(People[count].getCurrentYear() - People[count].getBirthYear());

                    birthYear.Text = People[count].getBirthYear().ToString();
                    Age.Text = People[count].getAge().ToString();

                    if (People[count].getBirthYear().ToString().Length != 4 || People[count].getCurrentYear().ToString().Length != 4)
                    {
                        MessageBox.Show("You must input the full year! e.g. yyyy");
                    }
                    else
                    {
                        People[count].DisplayInfo();

                        count++;
                    }
                }
            }
        }
    }
}
