package main

import (
  "fmt"
  "net/http"
)

func main() {
  resp, err := http.Get("http://shop.sportlaedchen.de")
  if err != nil {
    fmt.Println(err)
  }
  fmt.Println(resp.Header)
  defer resp.Body.Close()
}
