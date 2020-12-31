//Mark Schelkoph
//Assignment 4

class SavingsAccount extends Account
{
  private double interest;

  public SavingsAccount(double x, double i)
  {
    super(x);
    interest = i;
  }

  public void Compound()
  {
    setBalance((getBalance() * interest) + getBalance());
  }

  public String toString()
  {
    return String.format("Balance: " + getBalance() + "\nInterest: " + interest + "\n");
  }
}
