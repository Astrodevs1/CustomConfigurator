import fastify from 'fastify';
import { exec } from 'child_process';

const app = fastify({ logger: true });

app.get('/', async (request, reply) => {

    exec('python3 ../scripts/database.py', (error, stdout, stderr) => {
    if (error) {
      reply.code(500).send('Internal Server Error');
    } else {
      reply.send({ hello: 'world', pythonOutput: stdout });
    }
  });
});

const start = async () => {
  try {
    await app.listen(5432);
    app.log.info(`Server is listening on ${app.server.address()}`);
  } catch (err) {
    app.log.error(err);
    process.exit(1);
  }
};

start();
