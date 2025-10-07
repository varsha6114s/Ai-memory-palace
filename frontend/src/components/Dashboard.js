import React, { useState } from 'react';
import {
  Typography,
  Grid,
  Card,
  CardContent,
  CardActions,
  Button,
  Box,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
  Fab,
  CircularProgress,
} from '@mui/material';
import { Add as AddIcon, AccountBalance as PalaceIcon } from '@mui/icons-material';
import { useQuery, useMutation, useQueryClient } from 'react-query';
import { useForm } from 'react-hook-form';
import { Link } from 'react-router-dom';
import { usersAPI } from '../services/api';
import { useAuth } from '../contexts/AuthContext';
import toast from 'react-hot-toast';

const Dashboard = () => {
  const [createDialogOpen, setCreateDialogOpen] = useState(false);
  const { user } = useAuth();
  const queryClient = useQueryClient();
  const { register, handleSubmit, reset, formState: { errors } } = useForm();

  const { data: palaces, isLoading } = useQuery(
    'memory-palaces',
    () => usersAPI.getMemoryPalaces().then(res => res.data.memory_palaces),
    {
      onError: (error) => {
        toast.error('Failed to load memory palaces');
      }
    }
  );

  const createPalaceMutation = useMutation(
    (data) => usersAPI.createMemoryPalace(data),
    {
      onSuccess: () => {
        queryClient.invalidateQueries('memory-palaces');
        setCreateDialogOpen(false);
        reset();
        toast.success('Memory palace created successfully!');
      },
      onError: (error) => {
        toast.error('Failed to create memory palace');
      }
    }
  );

  const onSubmit = (data) => {
    createPalaceMutation.mutate(data);
  };

  if (isLoading) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center" minHeight="50vh">
        <CircularProgress />
      </Box>
    );
  }

  return (
    <Box>
      <Typography variant="h3" component="h1" gutterBottom>
        Welcome back, {user?.username}!
      </Typography>
      
      <Typography variant="h5" component="h2" gutterBottom sx={{ mt: 4, mb: 3 }}>
        Your Memory Palaces
      </Typography>

      {palaces && palaces.length > 0 ? (
        <Grid container spacing={3}>
          {palaces.map((palace) => (
            <Grid item xs={12} sm={6} md={4} key={palace.id}>
              <Card>
                <CardContent>
                  <Box display="flex" alignItems="center" mb={2}>
                    <PalaceIcon color="primary" sx={{ mr: 1 }} />
                    <Typography variant="h6" component="h3">
                      {palace.title}
                    </Typography>
                  </Box>
                  <Typography variant="body2" color="text.secondary" paragraph>
                    {palace.description || 'No description provided'}
                  </Typography>
                  <Typography variant="caption" color="text.secondary">
                    {palace.rooms_count} rooms • Created {new Date(palace.created_at).toLocaleDateString()}
                  </Typography>
                </CardContent>
                <CardActions>
                  <Button
                    size="small"
                    component={Link}
                    to={`/palace/${palace.id}`}
                    variant="contained"
                  >
                    Enter Palace
                  </Button>
                </CardActions>
              </Card>
            </Grid>
          ))}
        </Grid>
      ) : (
        <Box textAlign="center" py={8}>
          <PalaceIcon sx={{ fontSize: 80, color: 'text.secondary', mb: 2 }} />
          <Typography variant="h6" color="text.secondary" gutterBottom>
            No memory palaces yet
          </Typography>
          <Typography variant="body2" color="text.secondary" paragraph>
            Create your first memory palace to start organizing your knowledge
          </Typography>
          <Button
            variant="contained"
            startIcon={<AddIcon />}
            onClick={() => setCreateDialogOpen(true)}
          >
            Create Your First Palace
          </Button>
        </Box>
      )}

      <Fab
        color="primary"
        aria-label="add"
        sx={{ position: 'fixed', bottom: 16, right: 16 }}
        onClick={() => setCreateDialogOpen(true)}
      >
        <AddIcon />
      </Fab>

      <Dialog open={createDialogOpen} onClose={() => setCreateDialogOpen(false)} maxWidth="sm" fullWidth>
        <DialogTitle>Create New Memory Palace</DialogTitle>
        <DialogContent>
          <Box component="form" onSubmit={handleSubmit(onSubmit)} sx={{ mt: 1 }}>
            <TextField
              fullWidth
              label="Palace Title"
              margin="normal"
              {...register('title', {
                required: 'Title is required'
              })}
              error={!!errors.title}
              helperText={errors.title?.message}
            />
            <TextField
              fullWidth
              label="Description (optional)"
              multiline
              rows={3}
              margin="normal"
              {...register('description')}
            />
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setCreateDialogOpen(false)}>Cancel</Button>
          <Button
            onClick={handleSubmit(onSubmit)}
            variant="contained"
            disabled={createPalaceMutation.isLoading}
          >
            {createPalaceMutation.isLoading ? 'Creating...' : 'Create Palace'}
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
};

export default Dashboard;