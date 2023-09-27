// C# Team Interface
public class Team{
	public string teamName;
	public int noOfPlayers;

	public Team(string teamName, int noOfPlayers){
		this.teamName = teamName;
		this.noOfPlayers = noOfPlayers;
	}

	public void AddPlayer(int count){
		noOfPlayers += count;
	}

	public bool RemovePlayer(int count){
		if noOfPlayers < count{
			return false;
		}
		noOfPlayers -= count;
		return true;
	}

}

public class Subteam: Team{
	public Subteam(string teamName, int noOfPlayers): base(teamName, noOfPlayrs){

	}

	public void ChangeTeamName(string name){
		teamName = name;
	}
}