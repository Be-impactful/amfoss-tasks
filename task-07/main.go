package main

import (
	"strconv"
	"syscall/js"
)

func increment(this js.Value, args []js.Value) any {
	element := js.Global().Get("document").Call("getElementById", "number")
	if element.Get("textContent").String() != "Go!" {
		number, err := strconv.ParseInt(element.Get("textContent").String(), 10, 64)
		if err != nil {
			return map[string]any{"error": err.Error()}
		}
		number += int64(args[0].Int())
		element.Set("textContent", number)
		return map[string]any{"curr_value": number}
	} else {
		element.Set("textContent", 1)
		return map[string]any{"curr_value": 1}
	}
}

func decrement(this js.Value, args []js.Value) any {
	element := js.Global().Get("document").Call("getElementById", "number")
	if element.Get("textContent").String() != "Go!" {
		number, err := strconv.ParseInt(element.Get("textContent").String(), 10, 64)
		if err != nil {
			return map[string]any{"error": err.Error()}
		}
		number -= int64(args[0].Int())
		element.Set("textContent", number)
		return map[string]any{"curr_value": number}
	} else {
		element.Set("textContent", -1)
		return map[string]any{"curr_value": -1}
	}
}

func reset(this js.Value, args []js.Value) any {
	element := js.Global().Get("document").Call("getElementById", "number")
	element.Set("textContent", 0)
	return map[string]any{"curr_value": 0}
}

func main() {
	js.Global().Set("goIncrement", js.FuncOf(increment))
	js.Global().Set("goDecrement", js.FuncOf(decrement))
	js.Global().Set("goReset", js.FuncOf(reset))
	select {}
}
