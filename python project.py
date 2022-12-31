def calcAngle(h,m):
         
        # validate the input
        if (h < 0 or m < 0 or h > 24 or m > 60):
            print('Wrong input')
         
        if (h == 12):
            h = 0
        if (m == 60):
            m = 0
            h += 1;
            if(h>12):
                   h = h-12;
         
        hour_angle = 0.5 * (h * 60 + m)
        minute_angle = 6 * m
         
        # Find the difference between two angles
        angle = abs(hour_angle - minute_angle)
         
        # Return the smaller angle of two
        # possible angles
        angle = min(720 - angle, angle)
         
        return angle
 
# Driver Code
h = list(map(int,input().split (":")))
print('Angle ', calcAngle(h[0],h[1]))