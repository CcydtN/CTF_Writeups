exit = process.exit
argv = process.argv.slice(1)

d = 0
s = argv[1]
for (let i = 0; i < s.length; i++) {
    d = (d * 31 + s.charCodeAt(i)) % 93097
}
exit(+(d != 61343))
