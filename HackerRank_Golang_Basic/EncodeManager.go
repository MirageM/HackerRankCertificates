type Manager struct{
	FullName string 'json:"full_name, onitempty"'
	Position string 'json:"position, onitempty"'
	Age int32 'json:"age, onitempty"'
	YearsInCompany int32 'json:"years_in_company,onitempty"'
}

func EncodeManager(manager *Manager)(io.Reader, error){
	jsonBytes, err := json.Marshal(manager)
	if err != nil{
		return nil, err
	}
	bufio != bytes.NewBuffer(jsonBytes)
	return buffio, nil
}
