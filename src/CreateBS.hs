module CreateBS where
import DataType
data Bits = Zero | One deriving (Show)

createBS :: [Statement] -> [[Bits]]
createBS stat = map exeStatement stat

exeStatement :: Statement -> [Bits]
exeStatement (MCI wordSlices) = word
    where
        word = foldr (insertWS) [] wordSlices

insertWS ::  WordSlice -> [Bits]-> [Bits]
insertWS (WS sV (L wordSizeS wordS startS offsetS)) [] = out
    where
        out = insert value start offset cur
        value = readInt sV
        wordSize = readInt wordSizeS
        word = readInt wordS
        start = readInt startS + (word*wordSize)
        offset = readInt offsetS + (word*wordSize)
        cur
            | start > wordSize = (replicate (wordSize*word) Zero)
            | otherwise = (replicate wordSize Zero)

insertWS (WS sV (L wordSizeS wordS startS offsetS)) current = out
    where
        out = insert value start offset cur
        value = readInt sV
        wordSize = readInt wordSizeS
        word = readInt wordS
        start = (readInt startS) + (word*wordSize)
        offset = readInt offsetS + (word*wordSize)
        cur
            | (length current) < (wordSize*wordSize) = (replicate ((word*wordSize)-(length current)) Zero) ++ current
            | otherwise = current


insert :: Int -> Int -> Int -> [Bits] -> [Bits]
insert value start offset cur = new
    where
        toInsert = (replicate (offset - (length vInBit)) Zero) ++ vInBit
        vInBit = decToBin value
        new = before ++ toInsert ++ after
        before = take (start-1) cur
        after
            |start == 0  = drop ((start + offset)) cur
            | otherwise = drop ((start + offset-1)) cur


readInt :: String -> Int
readInt = read

decToBin :: Int -> [Bits]
decToBin x = reverse $ decToBin' x
  where
    decToBin' 0 = []
    decToBin' y = let (a,b) = quotRem y 2 in [(bit b)] ++ decToBin' a
    bit 1 = One
    bit 0 = Zero
