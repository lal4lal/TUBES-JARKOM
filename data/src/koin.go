package main
import "fmt"

func coinChange(nKoin []int, nominal int) int {
    dp := make([]int, nominal+1)
    for i := 1; i <= nominal; i++ {
        dp[i] = -1
    }
    dp[0] = 0

    for i := 1; i <= nominal; i++ {
        for _, koin := range nKoin {
            if koin <= i && dp[i-koin] != -1 {
                if dp[i] == -1 || dp[i] > 1+dp[i-koin] {
                    dp[i] = 1 + dp[i-koin]
                }
            }
        }
    }

    return dp[nominal]
}

func main() {
	nKoin := []int{1,6,10}
    nominal := 12

    jumlahKoin := coinChange(nKoin, nominal)
    fmt.Printf("Jumlah minimum koin yang dibutuhkan untuk membentuk %d adalah %d\n", nominal, jumlahKoin)
}