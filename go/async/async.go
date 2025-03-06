package main

import (
	"fmt"
	"net/http"
	"sync"
	"time"
)

// checks and prints a message if a website is up or down
func checkUrl(url string) {
	_, err := http.Get(url)
	if err != nil {
		fmt.Println(url, "is down !!!")
		return
	}
	fmt.Println(url, "is up and running.")
}

func SynchronousWay() {
	fmt.Println("Synchronous way")
	urls := []string{
		"https://www.easyjet.com/",
		"https://www.skyscanner.de/",
		"https://www.ryanair.com",
		"https://wizzair.com/",
		"https://www.swiss.com/",
	}
	for _, url := range urls {
		checkUrl(url)
	}
}

func GoroutineWay() {
	fmt.Println("Goroutine way")
	urls := []string{
		"https://www.easyjet.com/",
		"https://www.skyscanner.de/",
		"https://www.ryanair.com",
		"https://wizzair.com/",
		"https://www.swiss.com/",
	}
	for _, url := range urls {
		go checkUrl(url)
	}
	fmt.Println("Waiting for some secs...")
	time.Sleep(5 * time.Second)
}

func GoroutineWaitGroupWay() {
	fmt.Println("Goroutine way with WaitGroup")
	urls := []string{
		"https://www.easyjet.com/",
		"https://www.skyscanner.de/",
		"https://www.ryanair.com",
		"https://wizzair.com/",
		"https://www.swiss.com/",
	}
	// A WaitGroup waits for a collection of go routines to finish
	var wg sync.WaitGroup

	for _, u := range urls {
		// increment the wait group counter
		wg.Add(1)
		go func(url string) {
			// decrement the counter when the go routine completes
			defer wg.Done()
			// call the function
			checkUrl(url)
		}(u)
	}
	wg.Wait()
}

func GoChannelWay() {
	fmt.Println("Go channel way")

	urls := []string{
		"https://www.easyjet.com/",
		"https://www.skyscanner.de/",
		"https://www.ryanair.com",
		"https://wizzair.com/",
		"https://www.swiss.com/",
	}
	c := make(chan urlStatus)
	for _, url := range urls {
		go CheckUrlWithChan(url, c)
	}
	results := make([]urlStatus, len(urls))
	for i := range results {
		results[i] = <-c
		if results[i].status == "succeed" {
			fmt.Println((results[i].url), "is up")
		} else {
			fmt.Println((results[i].url), "is down!!")
		}
	}

}

func CheckUrlWithChan(url string, c chan urlStatus) {
	_, err := http.Get(url)
	if err != nil {
		c <- urlStatus{url, "error"}
	} else {
		c <- urlStatus{url, "succeed"}
	}
}

type urlStatus struct {
	url    string
	status string
}

func main() {
	// SynchronousWay()
	// GoroutineWay()
	// GoroutineWaitGroupWay()
	GoChannelWay()
}
