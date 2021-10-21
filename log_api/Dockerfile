FROM node:16
COPY . .
RUN npm install
RUN apt-get update
RUN apt-get install nano
CMD ["node", "out/server.js"]
# CMD ["./start.sh"]