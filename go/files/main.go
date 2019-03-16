package main

import (
	"fmt"
	"html/template"
	"net/http"
)

func main() {

	templates := template.Must(template.ParseFiles("/terraform/provisioners/roles/go/files/templates/index.html"))

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		if err := templates.ExecuteTemplate(w, "index.html", nil); err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
		}
	})

	fmt.Println(http.ListenAndServe(":80", nil))

}
