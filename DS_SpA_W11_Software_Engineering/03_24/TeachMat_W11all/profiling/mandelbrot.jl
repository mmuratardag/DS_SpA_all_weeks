
const w, h = 500, 500

const startX = -2.0
const startY = -1.5
const endX = 1.0
const endY = 1.5
const maxIter = 10

function mandelbrot()

    StartTime=time()

    for x in 1:w
        for y in 1:h
            i = maxIter
            c = Complex(
                x * ((endX - startX) / w)  + startX,
                y * ((endY - startY) / h) + startY
            )
            z = c
            while abs(z) < 2 && (i -= 1) > 0
                z = z^2 + c
            end
            intensity = i / maxIter
        end
    end

    StopTime=time() - StartTime;
    println("Done in ",StopTime," s.\n");
 end

mandelbrot()
