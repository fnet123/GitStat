from Utils import getPipOutput

class GitTool():
    def __init__(self):
        pass

    def getGitVersion(self):
        return getPipOutput(['git --version']).split('\n')[0]

    def getCommitCount(self, authorName=""):
        if "" == authorName:
            return getPipOutput(['git log --oneline', 'wc -l']).split('\n')[0]
        else:
            return getPipOutput(['git log --oneline --author=' + authorName, 'wc -l']).split('\n')[0]

    def getAuthorCount(self):
        return getPipOutput(['git shortlog -s']).split('\n')[0]

    def getCommitInfo(self, authorName='', startTime=0, endTime=0):
        if "" == authorName:
            return getPipOutput(['git log --pretty=tformat: --numstat', "gawk '{add+=$1; del+=$2; total+=$1-$2} END {printf\"%s,%s,%s\",add,del,total}'"]).split(",")
        else:
            return getPipOutput(['git log --pretty=tformat: --numstat --author=' + authorName, "gawk '{add+=$1; del+=$2; total+=$1-$2} END {printf\"%s,%s,%s\",add,del,total}'"]).split(",")
