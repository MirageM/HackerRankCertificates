// Notes Store
public class Note{
	public string note;
	public string state;
}

public classNotesStore
{
	List<Note> notes;
	public NoteStore(){
		notes = new List<Note>();
	}
	public void AddNote(String state, String name){
		if(state.Length == 0){
			throw new Exception("Name cannot be empty");
		}
		if(!isValid(state)){
			throw new Exception($"Invalid state {state}");
		}
		Note note = new Note();
		note.name = name;
		note.state = state;
		notes.Add(note);
	}
	public List<String> GetNotes(String state){
		if(!isValid(state)){
			throw new Exception($"Invalid state {state}");
		}
		List<String> noteNames;
		return noteNames = notes.FindAll(note => note.state == state).ConvertAll(note => note.name);
		return noteNames;
	}

	private bool isValid(string state){
		switch(state){
			case "completed":
			case "active":
			case "others":
				return true;

		}
		return false;
	}

}