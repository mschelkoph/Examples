//Mark Schelkoph
//Assignment 4

class CheckingAccount extends Account
{
  private int nextCheckNumber;

  public CheckingAccount(double x, int c)
  {
    super(x);
    nextCheckNumber = c;
  }

  public void orderChecks()
  {
    nextCheckNumber = nextCheckNumber + 1000;
  }

    public String toString()
  {
    return String.format("Balance: " + getBalance() + 
    "\nCheck Number: " + nextCheckNumber + "\n");
  }
}