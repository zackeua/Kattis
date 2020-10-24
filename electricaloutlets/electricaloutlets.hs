getInteger :: IO Integer
getInteger = fmap read getLine


main :: IO ()
main = do
    tot <- getInteger
    line <- getLine
    print line
