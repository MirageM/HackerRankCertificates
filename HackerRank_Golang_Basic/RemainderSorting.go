package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "sort"
    "strconv"
    "strings"
)


/*
 * Complete the 'RemainderSorting' function below (and other code for sorting if needed).
 *
 * The function is expected to return a STRING_ARRAY.
 * The function accepts STRING_ARRAY strArr as parameter.
 */

func RemainderSorting(strArr []string) []string {
    // Custom sorting function
    customSort := func(i, j int) bool {
        // Calculate the length modulo 3 for the two strings
        lenModuloI := len(strArr[i]) % 3
        lenModuloJ := len(strArr[j]) % 3
        
        // If the modulo values are different, sort by modulo value
        if lenModuloI != lenModuloJ{
            return lenModuloI < lenModuloJ
        }
        // If the modulo values are the same, sort alphabetically
        return strArr[i] < strArr[j]
    }
    
    // Use sort.Slice to sort strArr using the custom sorting function
    sort.Slice(strArr, customSort)
    return strArr
}
func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    strArrCount, err := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    checkError(err)

    var strArr []string

    for i := 0; i < int(strArrCount); i++ {
        strArrItem := readLine(reader)
        strArr = append(strArr, strArrItem)
    }

    result := RemainderSorting(strArr)

    for i, resultItem := range result {
        fmt.Fprintf(writer, "%s", resultItem)

        if i != len(result) - 1 {
            fmt.Fprintf(writer, "\n")
        }
    }

    fmt.Fprintf(writer, "\n")

    writer.Flush()
}

func readLine(reader *bufio.Reader) string {
    str, _, err := reader.ReadLine()
    if err == io.EOF {
        return ""
    }

    return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
    if err != nil {
        panic(err)
    }
}
