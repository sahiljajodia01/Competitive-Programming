# https://leetcode.com/explore/featured/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3346/


###### Edit Distance where Insertion, Deletion and Substitution is allowed is called as Levenshtien Distance #######
class Solution:
    def minDistance(self, A: str, B: str) -> int:
        dp = []
        for i in range(len(A)+1):
            temp = []
            for j in range(len(B)+1):
                temp.append(0)
            
            dp.append(temp)
    
        for i in range(len(B)+1):
            dp[0][i] = i
        
        for i in range(len(A)+1):
            dp[i][0] = i
        
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
        
        
        return dp[-1][-1]



##### Some Testcases #####
"horse"
"ros"
"intention"
"execution"
"sitting"
"kitten"
""
""
"s"
"a"
"s"
""
"s"
"s"
"xwjpxwvbbirhpxiswiztwiwyhvongsszpcbgfwznogkhbvxsosfkmykzoovlqvxwpysohskmqkevveiocfsdgksjcxvqmxfajgxhfapaqdhszrgsywuuotsrroirgxrcvnosxxbqzerncnffawjopeavgptdchdzmejhxagxemiqlrctkqksehqhzoyfawnavmeptvinlutcyywkwlkzcoujbbsfuxtxskuduwxjaeqonrdjaswletcgdlrlwuylsjszwzshkpumeaugyhpdkwkdbftgzxkuwmhekljgoacpoutszddhcpzomzsbjmqqonfnesqptqckzpyxraumxqocybdmzqmetrtjdfahuvzkxpzatnttqqbdzdojlvwtetaklfqtoamoozvxpvcbhxrjiqfkdpfmhlhacxhkvvskptxzagurrzobffxtmbfwgpcpdqnrhxamtpyvwxudajtzznoqezfxlarxdbpdyughtrtiapjrcwcsdqjdeunomvrqcjcocndpzjbbulmigztjmycuetdgbiwtyafbxulrqlseoqjjhixrvlujdxktwihihlsvnjzwkxvzqbhxijgbxstpaqyfzignypycqkapcpulqurxdfarqlzacjfsizujtifdjhjckwswyqhuuzjyhwtiszqacsfyhxnjnqoxtgzcloabmvujvuqkmaawemldilrbugmbezyusyxrqrxhxfnzzvvpmrsbfyvdyxpekznlrqdkcdmoeewkbebbdgwptjrierldedsraxifndotcfoyouhngitqstaodwaunqznjgluizhtalrflvzzhjqkpqmemvunkfpfvjdqsbnosiinehlevrixactjitdnfisvxfkbtckyrfmnwjlledrpfxcdvrlhkigeouwkpjevmeaagwnmfbvtyfuetdobcsxmakvbaelyocnojikygnsygpuvahbayqgqbingfepkkrjaymqjstyfclgcpniipatvcokrvvuhctsdinozqzmtewbgfvmtdnvfkxqielamapgmjqumydlfghfnsaeykkwuxanbkhjimxevstizbhyxumszjueycipzbcqgsjazvjsbxpiknlifzbthhvuqbtmvqdxwwdlaazyrxzehqbbntoljocxzkaktfbsifzywtahpzpgvyxzmmvikbcjrvaehucunxfxojcurodbvr"
"wffqcifxeusxqwreyhigcravihfqjimpruyvchouyjuvadscskgjtggwjxooaoimmkvvliptntehjarlagjgnhaifgsfozreadiuwkogcvlevszaqvwxshquclchvsmwjlnlcukarzudqqmdilzukmsbthsqytjwnzdxktxvhhimecijrkisgsmrqymoueqqluwqyjhwjwkqwwjpbviqswxirupwzyoproenyjevfokacuisahrnywovvqusigqzddihbuzwsiseozaklbisugxnirzopxprnbrcvgwnchrykkqgalbskoxoalotdfacxzqmbtjfkxnxhgmxqnbfuyjyluobmuovonjsmiqyncqsntnuernywastphwkhjtzzpccniqunliidhwphorpdgzulrahwyfafdavjehuwylrubbtlmnqeryvvtstwvhtdauvgafqejkbtuyfhrqxdrnzoawdnswrbjomdihgwkkyeiruauxu"