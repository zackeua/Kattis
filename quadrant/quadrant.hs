
quadrant :: Double -> Double -> Integer
quadrant x y = if x >= 0
    then if y >= 0
        then 1
        else 4
    else if y >= 0
        then 2
        else 3

getDouble :: IO Double
getDouble = fmap read getLine

getInteger :: IO Integer
getInteger = fmap read getLine

main :: IO ()
main = do
    x <- getDouble
    y <- getDouble
    print (quadrant x y)
