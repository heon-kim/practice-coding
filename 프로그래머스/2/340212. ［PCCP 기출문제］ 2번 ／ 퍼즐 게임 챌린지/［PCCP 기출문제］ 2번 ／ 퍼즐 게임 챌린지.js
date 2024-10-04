function solution(diffs, times, limit) {
    let left = 1;
    let right = diffs.reduce((acc, cur) => Math.max(acc, cur), 1);
    
    const canSolveWithLevel = (level) => {
        let totalTime = 0;
        let prevTime = 0;

        for (let i = 0; i < diffs.length; i++) {
            const diff = diffs[i];
            const timeCur = times[i];

            if (diff <= level) {
                totalTime += timeCur;
            } else {
                totalTime += (diff - level) * (timeCur + prevTime) + timeCur;
            }

            prevTime = timeCur; 
        }

        return totalTime <= limit;
};

    while (left < right) {
        const mid = Math.floor((left + right) / 2);
        
        if (canSolveWithLevel(mid)) {
            right = mid; 
        } else {
            left = mid + 1;
        }
    }

    return left; 
}




