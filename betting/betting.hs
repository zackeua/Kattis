getInteger :: IO Integer
getInteger = fmap read getLine


main :: IO ()
main = do
    tot <- getInteger
    print (fromIntegral (100 - tot) / fromIntegral (tot) + 1)
    print ( fromIntegral tot / fromIntegral (100 - tot)  + 1)
