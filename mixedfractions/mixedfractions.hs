getString :: IO String
getString = getLine

splitString :: String  -> [String]
splitString x = fmap (words x)

listToNum :: [String] -> [Integer]
listToNum [] = []
listToNum (n:ns) = [read n] ++ listToNum ns

getFraction :: IO [Integer]
getFraction = fmap read getLine



main :: IO ()
main = do
    x <- getString
    print (x)
    print (listToNum (splitString (getString)))