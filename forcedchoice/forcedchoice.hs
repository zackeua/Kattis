toList :: String -> [Int]
toList x = map read $ words x

readLists :: Int -> [[Int]]
readLists 1 = do
    input <- getLine
    [toList input]
readLists x = do
    input <- getLine
    [toList input] ++ readLists (x-1)

main :: IO ()
main = do
    input <- getLine
    --print input
    let list = toList input
    let lists = readLists (list!!3)
    print lists