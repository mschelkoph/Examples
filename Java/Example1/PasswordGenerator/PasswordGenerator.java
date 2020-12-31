//Mark Schelkoph
//Assignment 2

public class PasswordGenerator
{
  private int n;
  private String word1;
  private String word2;
  private String word3;
  private String word4;
  private String word5;


  public PasswordGenerator(int num, String w1, String w2, String w3, String w4, String w5)
  {
    n = num;
    word1 = w1;
    word2 = w2;
    word3 = w3;
    word4 = w4;
    word5 = w5;
  }


  public void setN(int x)
  {
    n = x;
  }
  public int getN()
  {
    return n;
  }

  public void setWord1(String x)
  {
    word1 = x;
  }
  public String getWord1()
  {
    return word1;
  }

  public void setWord2(String x)
  {
    word2 = x;
  }
  public String getWord2()
  {
    return word2;
  }

  public void setWord3(String x)
  {
    word3 = x;
  }
  public String getWord3()
  {
    return word3;
  }

  public void setWord4(String x)
  {
    word4 = x;
  }
  public String getWord4()
  {
    return word4;
  }

  public void setWord5(String x)
  {
    word5 = x;
  }
  public String getWord5()
  {
    return word5;
  }

  public void setPhrase(String w1, String w2, String w3, String w4, String w5)
  {
    setWord1(w1);
    setWord2(w2);
    setWord3(w3);
    setWord4(w4);
    setWord5(w5);
  }
  public String getPhrase()
  {
    String x = getWord1() + " " + getWord2() + " " + getWord3() + " " + getWord4() + " " + getWord5();

    return x;
  }

  public int getPasswordLength()
  {
    return getPassword().length();
  }

  public String getPassword()
  {
    String password = "";

    String[] w = {getWord1(), getWord2(), getWord3(), getWord4(), getWord5()};

    for(int i = 0; i < w.length; i++)
    {
      if (getN() > w[i].length())
      {
        password = password + w[i];
      }
      else
      {
        password = password + w[i].substring(0, getN());
      }
    }
    return password;
  }
}
