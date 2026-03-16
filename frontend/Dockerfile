FROM node:18-alpine AS builder
# here this create .dist so we will build and move static files inside nginx root folder
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build


FROM nginx:stable-alpine3.23-slim

# this isn't vite this is create by create-react-app so its called ./build not ./dist
COPY --from=builder /app/build /usr/share/nginx/html 
# or you can copy the nginx.conf to inside docker compose file 
# the default.conf will be included inside nginx.conf
COPY --from=builder /app/default.conf /etc/nginx/conf.d/default.conf  

ARG REACT_APP_API_URL
ENV REACT_APP_API_URL=$REACT_APP_API_URL

EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]


