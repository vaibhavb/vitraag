export function timesince(when){
    console.log("Time Since " + when)
    var now = new Date()
    timesince = ((now - new Date(when)/1000))
    return (timesince)
}