class Solution:
    def minScoreTriangulation(self, polygonValues: list[int]) -> int:
        vertexCount = len(polygonValues)
        minScore = [[0] * vertexCount for _ in range(vertexCount)]

        for gap in range(2, vertexCount):
            for start in range(vertexCount - gap):
                end = start + gap
                currentMinScore = 1 << 30

                for mid in range(start + 1, end):
                    triangleScore = (
                        minScore[start][mid]
                        + minScore[mid][end]
                        + polygonValues[start] * polygonValues[mid] * polygonValues[end]
                    )
                    if triangleScore < currentMinScore:
                        currentMinScore = triangleScore

                minScore[start][end] = currentMinScore

        return minScore[0][vertexCount - 1]